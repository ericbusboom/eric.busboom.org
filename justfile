dev:
    hugo server --buildDrafts --port 1313

build:
    hugo --minify --buildDrafts

clean:
    rm -rf public resources
