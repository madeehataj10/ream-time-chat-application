import React from "react";
const Greeting = ({ name }) => {
return <h1>Hello, {name}!</h1>;
};
export default Greeting;
Using the Component in App.js
javascript
CopyEdit
import Greeting from "./Greeting";
function App() {
return (
<div>
<Greeting name="John" />
</div>
);
}
export default App;
b) JSX (JavaScript XML)
JSX allows writing HTML-like syntax inside JavaScript.
javascript
CopyEdit
const element = <h1>Hello, React!</h1>;
JSX gets converted to JavaScript before rendering.
c) Props (Properties)
Props allow passing data to components.
javascript
CopyEdit
const UserProfile = ({ username }) => {
return <p>Welcome, {username}!</p>;
};
// Usage
<UserProfile username="Alice" />
d) State Management
State stores dynamic values and is managed using the useState hook.
javascript
CopyEdit
import { useState } from "react";
const Counter = () => {
const [count, setCount] = useState(0);
return (
<div>
<p>Count: {count}</p>
<button onClick={() => setCount(count + 1)}>Increment</button>
</div>
);
};
State updates trigger re-renders, updating the UI.
e) Handling Events
React handles events like clicks using camelCase syntax.
javascript
CopyEdit
<button onClick={() => alert("Button Clicked!")}>Click Me</button>
f) useEffect Hook (Side Effects)
useEffect runs side effects (like fetching data) when a component mounts or updates.
javascript
CopyEdit
import { useEffect, useState } from "react";
const FetchData = () => {
const [data, setData] = useState([]);
useEffect(() => {
fetch("https://jsonplaceholder.typicode.com/posts")
.then(response => response.json())
.then(data => setData(data));
}, []); // Empty dependency array = runs once on mount
return (
<ul>
{data.slice(0, 5).map(post => (
<li key={post.id}>{post.title}</li>
))}
</ul>
);
};
g) React Router (Navigation)
To create multiple pages, use React Router.
bash
CopyEdit
npm install react-router-dom
Setup Routes
javascript
CopyEdit
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
const Home = () => <h2>Home Page</h2>;
const About = () => <h2>About Page</h2>;
function App() {
return (
<Router>
<nav>
<Link to="/">Home</Link>
<Link to="/about">About</Link>
</nav>
<Routes>
<Route path="/" element={<Home />} />
<Route path="/about" element={<About />} />
</Routes>
</Router>
);
}
export default App;
h) Fetching API Data
Using the fetch API or Axios to get data.
javascript
CopyEdit
import { useState, useEffect } from "react";
import axios from "axios";
const FetchUsers = () => {
const [users, setUsers] = useState([]);
useEffect(() => {
axios.get("https://jsonplaceholder.typicode.com/users")
.then(response => setUsers(response.data));
}, []);
return (
<ul>
{users.map(user => (
<li key={user.id}>{user.name}</li>
))}
</ul>
);
};
i) Global State Management (Redux, Context API)
For large applications, Redux or Context API can manage global state.
Using Context API
javascript
CopyEdit
import { createContext, useState, useContext } from "react";
// 1. Create context
const ThemeContext = createContext();
// 2. Provide context
const ThemeProvider = ({ children }) => {
const [theme, setTheme] = useState("light");
return (
<ThemeContext.Provider value={{ theme, setTheme }}>
{children}
</ThemeContext.Provider>
);
};
// 3. Consume context
const ThemedComponent = () => {
const { theme, setTheme } = useContext(ThemeContext);
return (
<div>
<p>Current Theme: {theme}</p>
<button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
Toggle Theme
</button>
</div>
);
};
// 4. Wrap App in Provider
function App() {
return (
<ThemeProvider>
<ThemedComponent />
</ThemeProvider>
);
}