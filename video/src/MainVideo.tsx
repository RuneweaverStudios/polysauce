import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';

export const MainVideo = () => {
  const { fps } = useVideoConfig();
  
  return (
    <AbsoluteFill style={{ background: '#0f1419' }}>
      <Sequence from={0} durationInFrames={90}>
        <IntroScene />
      </Sequence>
      
      <Sequence from={90} durationInFrames={120}>
        <HookScene />
      </Sequence>
      
      <Sequence from={210} durationInFrames={150}>
        <StepOneScene />
      </Sequence>
      
      <Sequence from={360} durationInFrames={150}>
        <StepTwoScene />
      </Sequence>
      
      <Sequence from={510} durationInFrames={150}>
        <StepThreeScene />
      </Sequence>
      
      <Sequence from={660} durationInFrames={150}>
        <StepFourScene />
      </Sequence>
      
      <Sequence from={810} durationInFrames={150}>
        <ActivityMonitorScene />
      </Sequence>
      
      <Sequence from={960} durationInFrames={120}>
        <OutroScene />
      </Sequence>
    </AbsoluteFill>
  );
};

const IntroScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const logoScale = spring({ frame, fps, config: { damping: 200 } });
  const glowOpacity = interpolate(frame, [30, 60], [0, 0.6], { extrapolateRight: 'clamp' });
  const textOpacity = spring({ frame: frame - 30, fps, config: { damping: 200 } });
  
  return (
    <AbsoluteFill style={{
      background: 'radial-gradient(circle at 50% 50%, #00d4ff15, #0f1419 70%)',
      justifyContent: 'center',
      alignItems: 'center',
    }}>
      <div style={{
        width: 200,
        height: 200,
        borderRadius: 40,
        background: 'linear-gradient(135deg, #00d4ff, #7c3aed)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        fontSize: 80,
        fontWeight: 900,
        color: '#0f1419',
        transform: `scale(${logoScale})`,
        boxShadow: `0 0 80px rgba(0, 212, 255, ${glowOpacity})`,
      }}>
        P
      </div>
      <div style={{
        position: 'absolute',
        marginTop: 320,
        opacity: textOpacity,
        textAlign: 'center',
      }}>
        <h1 style={{
          fontSize: 64,
          fontWeight: 800,
          color: 'white',
          fontFamily: 'Inter, sans-serif',
          letterSpacing: '-0.02em',
        }}>
          Polysauce
        </h1>
      </div>
    </AbsoluteFill>
  );
};

const HookScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const text1Spring = spring({ frame, fps, config: { damping: 200 } });
  const text2Spring = spring({ frame: frame - 30, fps, config: { damping: 200 } });
  const text3Spring = spring({ frame: frame - 60, fps, config: { damping: 200 } });
  
  return (
    <AbsoluteFill style={{
      background: '#0f1419',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '0 80px',
    }}>
      <div style={{ textAlign: 'center' }}>
        <p style={{
          fontSize: 52,
          fontWeight: 700,
          color: '#00d4ff',
          fontFamily: 'Inter, sans-serif',
          opacity: text1Spring,
          transform: `translateY(${interpolate(text1Spring, [0, 1], [30, 0])}px)`,
          marginBottom: 40,
        }}>
          Copy traders with
        </p>
        <p style={{
          fontSize: 96,
          fontWeight: 900,
          background: 'linear-gradient(135deg, #00d4ff, #7c3aed)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          fontFamily: 'Inter, sans-serif',
          opacity: text2Spring,
          transform: `translateY(${interpolate(text2Spring, [0, 1], [30, 0])}px)`,
          marginBottom: 40,
        }}>
          90%+ Win Rates
        </p>
        <p style={{
          fontSize: 42,
          fontWeight: 500,
          color: '#8b95a5',
          fontFamily: 'Inter, sans-serif',
          opacity: text3Spring,
          transform: `translateY(${interpolate(text3Spring, [0, 1], [30, 0])}px)`,
        }}>
          Automated bot execution
        </p>
      </div>
    </AbsoluteFill>
  );
};

const StepOneScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const stepSpring = spring({ frame, fps, config: { damping: 200 } });
  const contentSpring = spring({ frame: frame - 20, fps, config: { damping: 200 } });
  
  return (
    <AbsoluteFill style={{
      background: 'linear-gradient(180deg, #0f1419 0%, #1a2332 100%)',
      padding: 80,
    }}>
      <div style={{ marginBottom: 60, opacity: stepSpring }}>
        <div style={{
          fontSize: 28,
          fontWeight: 600,
          color: '#00d4ff',
          fontFamily: 'IBM Plex Mono, monospace',
          marginBottom: 20,
        }}>
          STEP 01
        </div>
        <h2 style={{
          fontSize: 72,
          fontWeight: 800,
          color: 'white',
          fontFamily: 'Inter, sans-serif',
          lineHeight: 1.1,
        }}>
          Get Your API<br />Credentials
        </h2>
      </div>
      
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        gap: 24,
        opacity: contentSpring,
        transform: `translateY(${interpolate(contentSpring, [0, 1], [30, 0])}px)`,
      }}>
        {[
          'Navigate to Polymarket Settings',
          'Click your profile icon',
          'Go to Builder Settings',
          'Generate new API keys',
        ].map((text, i) => (
          <div key={i} style={{
            fontSize: 36,
            fontWeight: 500,
            color: '#e5e9f0',
            fontFamily: 'Inter, sans-serif',
            paddingLeft: 40,
            borderLeft: '4px solid #00d4ff',
          }}>
            {text}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

const StepTwoScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const stepSpring = spring({ frame, fps, config: { damping: 200 } });
  const warningSpring = spring({ frame: frame - 40, fps, config: { damping: 200 } });
  
  return (
    <AbsoluteFill style={{
      background: 'linear-gradient(180deg, #0f1419 0%, #1a2332 100%)',
      padding: 80,
    }}>
      <div style={{ marginBottom: 60, opacity: stepSpring }}>
        <div style={{
          fontSize: 28,
          fontWeight: 600,
          color: '#00d4ff',
          fontFamily: 'IBM Plex Mono, monospace',
          marginBottom: 20,
        }}>
          STEP 02
        </div>
        <h2 style={{
          fontSize: 72,
          fontWeight: 800,
          color: 'white',
          fontFamily: 'Inter, sans-serif',
          lineHeight: 1.1,
        }}>
          Save Your Keys<br />Securely
        </h2>
      </div>
      
      <div style={{
        background: 'rgba(245, 158, 11, 0.1)',
        border: '2px solid #f59e0b',
        borderRadius: 20,
        padding: 40,
        opacity: warningSpring,
        transform: `scale(${interpolate(warningSpring, [0, 1], [0.95, 1])})`,
      }}>
        <div style={{
          fontSize: 36,
          fontWeight: 700,
          color: '#f59e0b',
          marginBottom: 20,
        }}>
          ⚠️ Security Warning
        </div>
        <p style={{
          fontSize: 32,
          color: '#e5e9f0',
          fontFamily: 'Inter, sans-serif',
          lineHeight: 1.5,
        }}>
          Never share your API keys or private key!
          These give full access to your account.
        </p>
      </div>
    </AbsoluteFill>
  );
};

const StepThreeScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const stepSpring = spring({ frame, fps, config: { damping: 200 } });
  const metricsSpring = spring({ frame: frame - 30, fps, config: { damping: 200 } });
  
  return (
    <AbsoluteFill style={{
      background: 'linear-gradient(180deg, #0f1419 0%, #1a2332 100%)',
      padding: 80,
    }}>
      <div style={{ marginBottom: 60, opacity: stepSpring }}>
        <div style={{
          fontSize: 28,
          fontWeight: 600,
          color: '#00d4ff',
          fontFamily: 'IBM Plex Mono, monospace',
          marginBottom: 20,
        }}>
          STEP 03
        </div>
        <h2 style={{
          fontSize: 72,
          fontWeight: 800,
          color: 'white',
          fontFamily: 'Inter, sans-serif',
          lineHeight: 1.1,
        }}>
          Choose a Winning<br />Trader
        </h2>
      </div>
      
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: 24,
        opacity: metricsSpring,
      }}>
        <div style={{
          background: 'rgba(16, 185, 129, 0.1)',
          border: '1px solid #10b981',
          borderRadius: 16,
          padding: 32,
          textAlign: 'center',
        }}>
          <div style={{ fontSize: 56, fontWeight: 800, color: '#10b981' }}>90%+</div>
          <div style={{ fontSize: 24, color: '#8b95a5', marginTop: 8 }}>Win Rate</div>
        </div>
        <div style={{
          background: 'rgba(124, 58, 237, 0.1)',
          border: '1px solid #7c3aed',
          borderRadius: 16,
          padding: 32,
          textAlign: 'center',
        }}>
          <div style={{ fontSize: 56, fontWeight: 800, color: '#7c3aed' }}>50+</div>
          <div style={{ fontSize: 24, color: '#8b95a5', marginTop: 8 }}>Trades</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const StepFourScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const stepSpring = spring({ frame, fps, config: { damping: 200 } });
  const configSpring = spring({ frame: frame - 20, fps, config: { damping: 200 } });
  
  return (
    <AbsoluteFill style={{
      background: 'linear-gradient(180deg, #0f1419 0%, #1a2332 100%)',
      padding: 80,
    }}>
      <div style={{ marginBottom: 60, opacity: stepSpring }}>
        <div style={{
          fontSize: 28,
          fontWeight: 600,
          color: '#00d4ff',
          fontFamily: 'IBM Plex Mono, monospace',
          marginBottom: 20,
        }}>
          STEP 04
        </div>
        <h2 style={{
          fontSize: 72,
          fontWeight: 800,
          color: 'white',
          fontFamily: 'Inter, sans-serif',
          lineHeight: 1.1,
        }}>
          Configure the<br />Desktop App
        </h2>
      </div>
      
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        gap: 20,
        opacity: configSpring,
      }}>
        {[
          'Paste your API credentials',
          'Add target wallet address',
          'Set risk parameters',
          'Start the bot',
        ].map((text, i) => (
          <div key={i} style={{
            fontSize: 32,
            fontWeight: 500,
            color: '#e5e9f0',
            fontFamily: 'Inter, sans-serif',
            paddingLeft: 32,
            borderLeft: '4px solid #7c3aed',
          }}>
            {text}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

const ActivityMonitorScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const titleSpring = spring({ frame, fps, config: { damping: 200 } });
  const activitySpring = spring({ frame: frame - 30, fps, config: { damping: 200 } });
  const pulseOpacity = interpolate(frame % 30, [0, 15, 30], [0.5, 1, 0.5], { extrapolateRight: 'clamp' });
  
  return (
    <AbsoluteFill style={{
      background: 'linear-gradient(180deg, #0f1419 0%, #1a2332 100%)',
      padding: 80,
    }}>
      <div style={{ marginBottom: 60, opacity: titleSpring }}>
        <h2 style={{
          fontSize: 72,
          fontWeight: 800,
          color: 'white',
          fontFamily: 'Inter, sans-serif',
          lineHeight: 1.1,
        }}>
          Watch It Work
        </h2>
      </div>
      
      <div style={{
        background: '#1a2332',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        borderRadius: 20,
        padding: 40,
        opacity: activitySpring,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginBottom: 24 }}>
          <div style={{
            width: 16,
            height: 16,
            borderRadius: '50%',
            background: '#10b981',
            boxShadow: `0 0 20px rgba(16, 185, 129, ${pulseOpacity})`,
          }} />
          <span style={{ fontSize: 28, color: '#10b981', fontWeight: 600 }}>
            Live Activity Monitor
          </span>
        </div>
        <p style={{
          fontSize: 32,
          color: '#8b95a5',
          fontFamily: 'Inter, sans-serif',
        }}>
          Bot automatically copies trades in real-time
        </p>
      </div>
    </AbsoluteFill>
  );
};

const OutroScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const textSpring = spring({ frame, fps, config: { damping: 200 } });
  const ctaSpring = spring({ frame: frame - 30, fps, config: { damping: 200 } });
  const buttonScale = spring({ frame: frame - 50, fps, config: { damping: 8, stiffness: 200 } });
  
  return (
    <AbsoluteFill style={{
      background: 'radial-gradient(circle at 50% 50%, #00d4ff15, #0f1419 70%)',
      justifyContent: 'center',
      alignItems: 'center',
      padding: 80,
    }}>
      <div style={{ textAlign: 'center' }}>
        <h2 style={{
          fontSize: 80,
          fontWeight: 800,
          color: 'white',
          fontFamily: 'Inter, sans-serif',
          marginBottom: 40,
          opacity: textSpring,
        }}>
          Start Copying<br />Today
        </h2>
        
        <div style={{
          background: 'linear-gradient(135deg, #00d4ff, #7c3aed)',
          borderRadius: 20,
          padding: '32px 80px',
          display: 'inline-block',
          opacity: ctaSpring,
          transform: `scale(${buttonScale})`,
          boxShadow: '0 20px 60px rgba(0, 212, 255, 0.3)',
        }}>
          <span style={{
            fontSize: 48,
            fontWeight: 700,
            color: '#0f1419',
            fontFamily: 'Inter, sans-serif',
          }}>
            polysauce.xyz
          </span>
        </div>
      </div>
    </AbsoluteFill>
  );
};
