import { useState } from "react";

const NewExpense = (props) => {
  const [enteredTitle, setEnteredTitle] = useState("");
  const [enteredAmountLocal, setEnteredAmountLocal] = useState("");
  const [enteredAmountTarget, setEnteredAmountTarget] = useState("");
  const [enteredDate, setEnteredDate] = useState("");

  const titleChangeHandler = (event) => {
    setEnteredTitle(event.target.value);
  };

  const amountLocalChangeHandler = (event) => {
    setEnteredAmountLocal(event.target.value);
  };

  const amountTargetChangeHandler = (event) => {
    setEnteredAmountTarget(event.target.value);
  };

  const dateChangeHandler = (event) => {
    setEnteredDate(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const expenseData = {
      title: enteredTitle,
      amountLocal: +enteredAmountLocal,
      amountTarget: +enteredAmountTarget,
      date: new Date(enteredDate),
    };

    props.onSaveExpenseData(expenseData);
    setEnteredTitle("");
    setEnteredAmountLocal("");
    setEnteredAmountTarget("");
    setEnteredDate("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="my-8 items-center">
        <h2 className="border-b">Add new transaction</h2>
        <div className="mt-2 px-1">
          <div className="mt-2 px-1">
            <label className="text-sm">Title</label>
            <input
              className="block w-full bg-white border px-2 py-1"
              type="text"
              value={enteredTitle}
              onChange={titleChangeHandler}
            />
          </div>
          <div className="mt-2 px-1">
            <label className="text-sm">Amount Local</label>
            <input
              className="block w-full bg-white border px-2 py-1 mt-1"
              type="number"
              min="0.01"
              step="0.01"
              value={enteredAmountLocal}
              onChange={amountLocalChangeHandler}
            />
          </div>
          <div className="mt-2 px-1">
            <label className="text-sm">Amount Converted</label>
            <input
              className="block w-full bg-white border px-2 py-1 mt-1"
              type="number"
              min="0.01"
              step="0.01"
              value={enteredAmountTarget}
              onChange={amountTargetChangeHandler}
            />
          </div>
          <div className="mt-1 leading-none">
            <label className="text-sm">Date</label>
            <input
              className="block w-full bg-white border px-2 py-1 mt-1"
              type="date"
              min="2019-01-01"
              max="2023-12-31"
              value={enteredDate}
              onChange={dateChangeHandler}
            />
          </div>
        </div>
        <div className="mt-2">
          <button
            className="w-full py-1 bg-purple-400 hover:bg-purple-500 text-white border px-2 mt-1"
            type="submit"
          >
            Add Expense
          </button>
          <button
            className="w-full py-1 bg-purple-400 hover:bg-purple-500 text-white border px-2 mt-1"
            type="button"
            onClick={props.onCancel}
          >
            Cancel
          </button>
        </div>
      </div>
    </form>
  );
};

export default NewExpense;
