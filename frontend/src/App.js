import logo from './logo.svg';
import './App.css';
import NewExpense from './components/NewExpense/NewExpense';
import { useState } from 'react';

const DATA = [];

function App() {

  const [expenses, setExpenses] = useState(DATA);

  const submitExpenseHandler = (expense) => {
    setExpenses((prevExpenses) => {
      return [expense, ...prevExpenses];
    });
    console.log(expenses);
  };

  return (
    <div className="App">
      <NewExpense onAddExpense={submitExpenseHandler} />
    </div>
  );
}

export default App;
