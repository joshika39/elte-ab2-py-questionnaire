import React, {useEffect, useState} from 'react';
import './App.css';

const Flashcard = ({ question, answer, onFlip, onMarkKnown, flipped, key }) => (
  <div className="flashcard" onClick={onFlip} key={key}>
    <div>{flipped ? answer : question}</div>
    {flipped && <button onClick={onMarkKnown}>Mark as Known</button>}
  </div>
);

const App = () => {
  const [questions, setQuestions] = useState([]);
  const [knownQuestions, setKnownQuestions] = useState(
    JSON.parse(localStorage.getItem("knownQuestions") || "[]")
  );

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL)
      .then((res) => res.json())
      .then((data) => setQuestions(data))
      .catch(console.error);
  }, []);

  const markAsKnown = (index) => {
    const updated = [...knownQuestions, questions[index].question];
    setKnownQuestions(updated);
    localStorage.setItem("knownQuestions", JSON.stringify(updated));
  };

  const filteredQuestions = questions.filter(
    (q) => !knownQuestions.includes(q.question)
  );

  return (
    <div>
      <h1>Flashcards</h1>
      {filteredQuestions.length > 0 ? (
        filteredQuestions.map((q, i) => (
          <Flashcard
            key={i}
            question={q.question}
            answer={q.answer}
            flipped={false}
            onFlip={() => {}}
            onMarkKnown={() => markAsKnown(i)}
          />
        ))
      ) : (
        <p>You've mastered all questions!</p>
      )}
    </div>
  );
};

export default App;
