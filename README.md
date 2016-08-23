# blog.likewise.org

This repo contains my blog posts and the Pelican framework files used to publish them.

To bring up a development server on http://localhost:8000/:

```
make html
make devserver
```

To stop the dev server:

```
make stopserver
```

To publish with prod settings:

```
make s3_upload_dry_run
make s3_upload
```
