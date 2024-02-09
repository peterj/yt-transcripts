# YT video transcripts

1. Set the OpenAI API key in the `.env` file.
2. Set the YT video URL in the `transcribe.py` file and run it:

```shell
python transcribe.py
```

3. The transcript will be saved in the `transcripts` folder.

4. Copy the transcript JSON file to the `/web/src/app/data` folder (and/or update the import in the page.tsx file)

5. Run the web app (from the `/web` folder):

```shell
npm install
npm run dev
```
