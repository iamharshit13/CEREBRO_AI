import Link from 'next/link'
export default function Home() {
  return (
    <div style={{padding: '2rem'}}>
      <h1>Cerebro AI</h1>
      <p>GPT RAG wrapper demo scaffold.</p>
      <p><Link href="/chat">Open Chat</Link></p>
    </div>
  )
}
