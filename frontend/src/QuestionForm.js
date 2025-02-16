import { useState } from "react";
import axios from "axios";
import "./QuestionForm.css"; // Import updated CSS

const api = axios.create({
  baseURL: "http://localhost:8000",
});

function QuestionForm() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [documents, setDocuments] = useState([]);

  const handleSubmit = async (e) => {
    setAnswer("");
    e.preventDefault();
    console.log("Your Question: ", question);
    const response = await api.post("/chat", { message: question });
    setAnswer(response.data.answer);
    setDocuments(response.data.documents);
  };

  const handleIndex = async (e) => {
    e.preventDefault();
    setAnswer("");
    const response = await api.get("/Indexing", { message: question });
    setAnswer(response.data.response);
  };

  return (
    <div className="wrapper">
      {/* <h1 className="title">Welcome to Fullstack RAG!</h1> */}
      <div className="card">
        <form className="form">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            className="input"
            placeholder="Ask a question..."
          />
          <button type="submit" onClick={handleSubmit} className="button submit-btn">
            Submit
          </button>
          <button type="submit" onClick={handleIndex} className="button index-btn">
            Index
          </button>
        </form>
        <div className="result-container">
          <h2 className="heading">Answer:</h2>
          <p className="text">{answer || "No response yet..."}</p>
          <h2 className="heading">Documents:</h2>
          <p className="text">{documents || "No documents available..."}</p>
        </div>
      </div>
    </div>
  );
}

export default QuestionForm;
