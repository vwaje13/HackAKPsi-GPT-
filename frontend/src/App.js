import React, { useState } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [isThinking, setIsThinking] = useState(false);

  const handleInput = (e) => {
    setInput(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSubmit();
    }
  };

  const handleSubmit = () => {
    if (!input.trim()) return;
    const newMessages = [...messages, { text: input, sender: "user" }];
    setMessages(newMessages);
    setInput("");
    setIsThinking(true);

    // Simulate an API call for bot response
    setTimeout(() => {
      const botResponse = "This is a response from the bot.";
      setIsThinking(false);
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: botResponse, sender: "bot" },
      ]);
    }, 2000);
  };

  return (
    <div className="App">
      <header className="App-header">MU RHO FAQ</header>
      <div className="message-container">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {isThinking && <div className="blob"></div>}
      </div>
      <div className="input-area">
        <input
          value={input}
          onChange={handleInput}
          onKeyPress={handleKeyPress}
          placeholder="Type your message..."
        />
        <button onClick={handleSubmit}>Send</button>
      </div>
    </div>
  );
}

export default App;
