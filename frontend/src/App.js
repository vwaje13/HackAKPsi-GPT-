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
    const userMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsThinking(true);

    fetch("http://localhost:5000/process-csv", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: input }),
    })
      .then((response) => response.json())
      .then((data) => {
        setIsThinking(false);
        if (data.error) {
          setMessages((prev) => [...prev, { text: data.error, sender: "bot" }]);
        } else {
          setMessages((prev) => [
            ...prev,
            { text: data.response, sender: "bot" },
          ]);
        }
      })
      .catch((error) => {
        console.error("There was an error!", error);
        setIsThinking(false);
        setMessages((prev) => [
          ...prev,
          { text: "Failed to fetch response.", sender: "bot" },
        ]);
      });
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
