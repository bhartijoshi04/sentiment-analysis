import React, { useState } from "react";
import axios from "axios";

function FileUpload({ onResults }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please select a file!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTczNjk2MDM5OC41ODk4NzI4fQ.Y2Hs8-2LTIQze72WoGamSaCOS6rWaVcJaCgeSa5KJKw"; // Replace with token fetching logic
      const response = await axios.post("http://127.0.0.1:8000/analyze-csv/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${token}`,
        },
      });
      onResults(response.data.results);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Failed to analyze file. Check console for details.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Upload CSV File</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".csv" onChange={handleFileChange} />
        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>
    </div>
  );
}

export default FileUpload;

