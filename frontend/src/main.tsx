import ReactDOM from "react-dom/client";
import App from "./pages/App.tsx";
import "./styles/globals.css";
import { BrowserRouter } from "react-router";

const root = document.getElementById("root");

ReactDOM.createRoot(root!).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
