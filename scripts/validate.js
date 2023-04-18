const Ajv = require('ajv');
const AjvFormats = require('ajv-formats');
const eventSchema = require ('../schemas/events/v1/events.json');
const fs = require('fs/promises');
const { readFileSync } = require('fs');
const { resolve, join } = require('path');
const betterAjvErrors = require('better-ajv-errors').default;

const getValidDataSchemas = (eventSchema) => eventSchema.oneOf.map(o => o.properties.dataschema.const);
const isDataSchemaConstError = (e) => e.instancePath === '/dataschema' && e.keyword === 'const';
const isMainOneOf = (e) => e.instancePath === '' && e.schemaPath === '#/oneOf' && e.keyword === 'oneOf';

const validateJson = (content, filename, validator) => {
    const data = JSON.parse(content);

    if (!validator(data)) {
        // Update the errors to help provide a more useful message.
        // This is possible because the main schema always has oneOf with the dataschema options.

        let errors = [...validator.errors].filter(e => !isMainOneOf(e));

        const validDataSchemas = getValidDataSchemas(eventSchema);
        const dataschemaErrors = errors.filter(isDataSchemaConstError).length;

        errors = errors.filter(e => !isDataSchemaConstError(e));

        if (validDataSchemas.length === dataschemaErrors) {
            errors.push({
                instancePath: '/dataschema',
                keyword: 'enum',
                params: {
                    allowedValues: validDataSchemas
                },
                message: 'must use one of the allowed values'
            });
        }

        console.log('Invalid json', filename ? `: ${filename}` : '');
        const output = betterAjvErrors(eventSchema, data, errors, {
            format: 'cli',
            indent: 2
        });
        console.log(output);

        return false;
    }

    return true;
}

const ajv = new Ajv({
    loadSchema: async (uri) => {
        // Ensure we are loading all our schemas locally
        if (uri.startsWith('https://console.redhat.com/api/schemas')) {
            uri = 'file://' + resolve(uri.replace('https://console.redhat.com/api/', ''));
        }

        uri = new URL(uri);
        return JSON.parse(await fs.readFile(uri, 'utf8'));
    }
});

AjvFormats(ajv);

(async () => {
    const validator = await ajv.compileAsync(eventSchema);

    // Load all examples and ensure they are valid.
    const base = resolve('examples');
    const examples = await fs.readdir(base);
    let failedOutput = false;

    let input;
    try {
        input = readFileSync(process.stdin.fd).toString();
    } catch (e) {
        // Ignore error - if we couldn't load from stdin, it's probably empty
    }

    if (input) {
        failedOutput = !validateJson(input, undefined, validator);
    } else {
        for (const example of examples) {
            const data = await fs.readFile(join(base, example), 'utf8');
            if (!validateJson(data, example, validator)) {
                failedOutput = true;
            }
        }
    }

    if (failedOutput) {
        process.exit(1);
    }
})();
