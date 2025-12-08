import { Route, Routes } from "react-router";
import routes from "../routes/routes";

function App() {
  return (
    <Routes>
      {routes.map((route, index) => (
        <Route key={index} path={route.path} element={route.element}></Route>
      ))}
    </Routes>
  );
}

export default App;
