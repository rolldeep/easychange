const Card = (props) => {
  const classes = "p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex space-x-4" + props.className;

  return <div className={classes}>{props.children}</div>;
};

export default Card;
