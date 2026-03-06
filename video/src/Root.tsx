import { Composition } from 'remotion';
import { MainVideo } from './MainVideo';

export const RemotionRoot = () => {
  return (
    <Composition
      id="MainVideo"
      component={MainVideo}
      durationInFrames={1080}
      fps={30}
      width={1080}
      height={1920}
    />
  );
};