# preposterus-to-hugo

Convert a [Preposter.us](https://preposter.us) blog posts into Markdown files.

Originally written to automate the migration of my Preposter.us blog to [Hugo](https://gohugo.io/), I've ressurected the project to perform a simular conversion for a [Next.js](nextjs.org/)-based blog.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Create an input directory: `mkdir input`
3. Create an output directory: `mkdir output`
4. Copy Preposter.us content into the `input` directory
5. Run the import script: `python import.py`
6. Examine results in the `output` directory


