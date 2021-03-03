import React, { useState, useEffect } from "react";

const Admin = (props) => {
  const [formData, setFormData] = useState(null);
  const [category, setCategory] = useState("");
  //   const [fetchNewData, setFetchNewData] = useState(false);

  useEffect(async () => {
    if (category === "") {
      setFormData(null);
      return;
    }

    await fetch(`/api/get-form-data/${category}/`)
      .then((res) => res.json())
      .then((data) => setFormData(data.Data));
  }, [category]);

  const generateForm = () => {
    if (!formData) return;

    let final = [<h2>Enter Details</h2>];

    formData.main_data.map((field) => {
      final.push(
        <>
          <label for={field}>{field}</label>
          <input type="text" name={field} id={field} />
        </>
      );
    });

    final.push(<h2>Additional Details</h2>);

    formData.details_data.map((field) => {
      final.push(
        <>
          <label for={field}>{field}</label>
          <input type="text" name={field} id={field} />
        </>
      );
    });

    return final;
  };

  return (
    <div>
      <h1>Admin</h1>
      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="">Select Category</option>
        <option value="TShirt">TShirt</option>
        <option value="StarMap">StarMap</option>
      </select>
      {generateForm()}
    </div>
  );
};

export default Admin;
