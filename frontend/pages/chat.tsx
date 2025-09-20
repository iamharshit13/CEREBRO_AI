import { useState } from 'react';

export default function ChatPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input) return;
    setLoading(true);
    const res = await fetch('http://localhost:8000/chat/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: input })
    });
    const data = await res.json();
    setMessages(prev => [...prev, {role: 'user', text: input}, {role: 'bot', text: data.response}]);
    setInput('');
    setLoading(false);
  };

  return (
    <div style={{padding: '2rem', maxWidth: 800}}>
      <h2>Chat</h2>
      <div style={{border: '1px solid #ddd', padding: '1rem', height: 360, overflow: 'auto'}}>
        {messages.map((m, i) => <p key={i}><strong>{m.role}:</strong> {m.text}</p>)}
      </div>
      <div style={{marginTop: 12, display: 'flex'}}>
        <input style={{flex: 1, padding: 8}} value={input} onChange={e => setInput(e.target.value)} placeholder='Type a message' />
        <button style={{marginLeft: 8}} onClick={sendMessage} disabled={loading}>{loading ? '...' : 'Send'}</button>
      </div>
    </div>
  )
}
