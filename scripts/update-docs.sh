mkdir -p docs
if [[ -d node_modules ]]; then
  npx @asyncapi/generator asyncapi.yaml @asyncapi/html-template --force-write -o docs/
else
  podman run --rm -it -v ${PWD}:/app/workspace:z \
    docker.io/asyncapi/generator ./workspace/asyncapi.yaml @asyncapi/html-template --force-write -o workspace/docs/
fi
