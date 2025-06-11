document.getElementById('checkBtn').addEventListener('click', function () {
    const testType = document.getElementById('testType').value;
    const unit = document.getElementById('unit').value;
    let value = parseFloat(document.getElementById('value').value);
    const output = document.getElementById('output');
  
    if (isNaN(value)) {
      output.textContent = 'Please enter a valid number.';
      output.className = 'result';
      return;
    }
  
    // Convert mmol/L to mg/dL if needed
    if (unit === 'mmol' && testType !== 'hba1c') {
      value = value * 18;
    }
  
    let result = '';
    let className = '';
  
    if (testType === 'fasting') {
      if (value < 70) {
        result = 'Low (Hypoglycemia)';
        className = 'low';
      } else if (value < 100) {
        result = 'Normal';
        className = 'normal';
      } else if (value < 126) {
        result = 'Pre-diabetic';
        className = 'prediabetic';
      } else {
        result = 'Diabetic';
        className = 'diabetic';
      }
    } else if (testType === 'postMeal') {
      if (value < 70) {
        result = 'Low (Hypoglycemia)';
        className = 'low';
      } else if (value < 140) {
        result = 'Normal';
        className = 'normal';
      } else if (value < 200) {
        result = 'Pre-diabetic';
        className = 'prediabetic';
      } else {
        result = 'Diabetic';
        className = 'diabetic';
      }
    } else if (testType === 'hba1c') {
      if (value < 4.0) {
        result = 'Low (Possible Hypoglycemia)';
        className = 'low';
      } else if (value < 5.7) {
        result = 'Normal';
        className = 'normal';
      } else if (value < 6.5) {
        result = 'Pre-diabetic';
        className = 'prediabetic';
      } else {
        result = 'Diabetic';
        className = 'diabetic';
      }
    }
  
    output.textContent = `Result: ${result}`;
    output.className = `result ${className}`;
  });
  