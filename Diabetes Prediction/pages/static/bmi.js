function calculateBMI() {
    const weight = parseFloat(document.getElementById("weight").value);
    const heightCm = parseFloat(document.getElementById("height").value);
    const resultDiv = document.getElementById("result");
  
    if (isNaN(weight) || isNaN(heightCm) || weight <= 0 || heightCm <= 0) {
      resultDiv.textContent = "Please enter valid weight and height values.";
      resultDiv.style.color = "red";
      return;
    }
  
    const heightM = heightCm / 100;
    const bmi = weight / (heightM * heightM);
    let category = "";
  
    if (bmi < 18.5) {
      category = "Underweight";
    } else if (bmi < 24.9) {
      category = "Normal weight";
    } else if (bmi < 29.9) {
      category = "Overweight";
    } else {
      category = "Obesity";
    }
  
    resultDiv.textContent = `Your BMI is ${bmi.toFixed(1)} (${category})`;
    resultDiv.style.color = "#333";
  }
  