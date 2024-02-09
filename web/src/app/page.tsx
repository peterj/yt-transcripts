'use client';
import { useRef, useState } from 'react';
import ReactPlayer from 'react-player';
// TODO: replace with your own transcript
import Transcript from './data/transcript.json';

interface Word {
  start: number;
  end: number;
  word: string;
}

const VIDEO_URL = 'https://www.youtube.com/watch?v=hkgLxhrjfUE';
export default function Home() {
  const playerRef = useRef<ReactPlayer | null>(null);
  const [selectedWord, setSelectedWord] = useState<Word | null>(null);

  return (
    <main className='flex min-h-screen w-full flex-col items-center mt-12'>
      <div className='w-[600px] h-[480px] aspect-video'>
        <ReactPlayer
          ref={(p) => {
            playerRef.current = p;
          }}
          url={VIDEO_URL}
          playing={true}
          controls
          width='100%'
          height='100%'
        />
      </div>
      <div className='py-5'>
        {selectedWord && (
          <div className='text-xs font-mono'>
            {selectedWord.word} - {selectedWord.start}s - {selectedWord.end}s
          </div>
        )}
      </div>
      <div className=' w-full h-[400px] px-24'>
        <h3 className='py-2 font-medium text-xl'>Transcript</h3>
        {/* Convert all words to single spans to captutre click events */}
        {Transcript.words.map((word, index) => {
          return (
            <span
              key={index}
              className='inline-block px-1 transition duration-150 ease-in-out hover:bg-yellow-200 cursor-pointer'
              onClick={(e) => {
                setSelectedWord(word);
                playerRef.current?.seekTo(word.start);
              }}
            >
              {word.word}
            </span>
          );
        })}
      </div>
    </main>
  );
}
