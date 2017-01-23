# blog.likewise.org

This repo contains my blog posts and the Pelican framework files used to publish them.

To make a new post, just copy and rename an old file in `content/` or cat out a template:

```
# This assumes your current working dir is your blog's root dir:
cat > content/2016-08-20-my-test-post.md << EOL
Title: My title
Date: 2016-08-20 12:30
Category: Python
Tags: pelican, publishing
Slug: my-test-post
Authors: Your Name Here
Summary: Short version for index and feeds

This is the content of my test post.
EOL
```

To bring up a development server on http://localhost:8000/:

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt

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
