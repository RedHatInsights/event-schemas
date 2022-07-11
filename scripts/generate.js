const {
  quicktypeMultiFile,
  InputData,
  JSONSchemaInput,
  JSONSchemaStore,
} = require("quicktype-core");
const { execSync } = require("child_process");
const fs = require("fs/promises");
const path = require("path");
const { generate } = require("quicktype-core/dist/MarkovChain");
const BASE_JAVA_PACKAGE = 'com.redhat.cloud.event';
const BASE_JAVA_SRC_PATH = 'libraries/java/src/generated/java';
const BASE_GOLANG_SRC_PATH = 'libraries/golang';
const BASE_JS_SRC_PATH = 'libraries/js/src';
const BASE_PYTHON_SRC_PATH = 'libraries/python/src';
const BASE_RUBY_SRC_PATH = 'libraries/ruby/src';

class StaticJSONSchemaStore extends JSONSchemaStore {
  constructor() {
    super();
  }
  async fetch(address) {
    const contents = await fs.readFile(address);
    return JSON.parse(contents);
  }
}

async function generateFiles(repoRoot, subdir) {
  const versions = await fs.readdir(`${repoRoot}/schemas/${subdir}`);
  for (const version of versions) {
    const schemas = await fs.readdir(`${repoRoot}/schemas/${subdir}/${version}`);
    for (const schema of schemas) {
      const schemaPath = `${repoRoot}/schemas/${subdir}/${version}/${schema}`;
      const jsonSchemaString = await fs.readFile(schemaPath, {encoding: 'utf8'});
      const filename = path.basename(schemaPath);
      const schemaInput = new JSONSchemaInput(new StaticJSONSchemaStore());
      const inputData = new InputData();
      await schemaInput.addSource({
        name: filename.replace('.json', ''),
        uris: [schemaPath],
        schema: jsonSchemaString
      });
      inputData.addInput(schemaInput);
      await generateGoFiles(subdir, version, inputData, schema);
      await generateJavaFiles(subdir, version, inputData, schema);
      await generateJsFiles(subdir, version, inputData, schema);
      await generatePythonFiles(subdir, version, inputData, schema);
      await generateRubyFiles(subdir, version, inputData, schema);
    }
  }
}

async function generateGoFiles(subdir, version, inputData, schema) {
  const outputPath = `${BASE_GOLANG_SRC_PATH}/${subdir}/${version}`;
  const packageName = path.basename(subdir);
  const result = await quicktypeMultiFile({
    inputData,
    lang: "go",
    rendererOptions: {
      package: packageName,
    },
  });
  console.log(result);
  await fs.mkdir(outputPath, {recursive: true});
  const filename = `${schema.replaceAll('-', '_').replaceAll('.json', '.go')}`;
  for (const [_, contents] of result) {
    await fs.writeFile(`${outputPath}/${filename}`, contents.lines.join('\n'));
  }
}

async function generateJavaFiles(subdir, version, inputData, _schema) {
  const subPackage = `${subdir.replaceAll('/', '.')}.${version}`;
  const packageName = `${BASE_JAVA_PACKAGE}.${subPackage}`;
  const outputPath = `${BASE_JAVA_SRC_PATH}/${packageName.replaceAll('.', '/')}`;
  const result = await quicktypeMultiFile({
    inputData,
    lang: "java",
    rendererOptions: {
      package: packageName,
    },
  });
  await fs.mkdir(outputPath, {recursive: true});
  for (const [filename, contents] of result) {
    await fs.writeFile(`${outputPath}/${filename}`, contents.lines.join('\n'));
  }
}

async function generateJsFiles(subdir, version, inputData, schema) {
  const outputPath = `${BASE_JS_SRC_PATH}/${subdir}/${version}`;
  const packageName = path.basename(subdir);
  const result = await quicktypeMultiFile({
    inputData,
    lang: "js",
    rendererOptions: {
      package: packageName,
    },
  });
  console.log(result);
  await fs.mkdir(outputPath, {recursive: true});
  const filename = `${schema.replaceAll('-', '_').replaceAll('.json', '.js')}`;
  for (const [_, contents] of result) {
    await fs.writeFile(`${outputPath}/${filename}`, contents.lines.join('\n'));
  }
}

async function generatePythonFiles(subdir, version, inputData, schema) {
  const outputPath = `${BASE_PYTHON_SRC_PATH}/${subdir}/${version}`;
  const packageName = path.basename(subdir);
  const result = await quicktypeMultiFile({
    inputData,
    lang: "python",
    rendererOptions: {
      package: packageName,
    },
  });
  console.log(result);
  await fs.mkdir(outputPath, {recursive: true});
  const filename = `${schema.replaceAll('-', '_').replaceAll('.json', '.py')}`;
  for (const [_, contents] of result) {
    await fs.writeFile(`${outputPath}/${filename}`, contents.lines.join('\n'));
  }
}

async function generateRubyFiles(subdir, version, inputData, schema) {
  const outputPath = `${BASE_RUBY_SRC_PATH}/${subdir}/${version}`;
  const packageName = path.basename(subdir);
  const result = await quicktypeMultiFile({
    inputData,
    lang: "ruby",
    rendererOptions: {
      package: packageName,
    },
  });
  console.log(result);
  await fs.mkdir(outputPath, {recursive: true});
  const filename = `${schema.replaceAll('-', '_').replaceAll('.json', '.rb')}`;
  for (const [_, contents] of result) {
    await fs.writeFile(`${outputPath}/${filename}`, contents.lines.join('\n'));
  }
}

async function main() {
  const repoRoot = execSync("git rev-parse --show-toplevel", { encoding: 'utf8' }).trim();
  const apps = await fs.readdir(`${repoRoot}/schemas/apps/`);
  await generateFiles(repoRoot, 'core');
  for (const app of apps) {
    await generateFiles(repoRoot, `apps/${app}`);
  }
}

main();
