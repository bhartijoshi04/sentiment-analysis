import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import ResultsVisualization from "./components/ResultsVisualization";
import './App.css';

function App() {
  const [results, setResults] = useState(null);

  const handleResults = (data) => {
    setResults(data);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Sentiment Analysis Portal</h1>
      </header>
      
      <div className="content-container">
        <div className="file-upload-section">
          <h2>Upload Your File for Sentiment Analysis</h2>
          <FileUpload onResults={handleResults} />
        </div>

        {results && (
          <div className="results-section">
            <h2>Analysis Results</h2>
            <ResultsVisualization results={results} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
