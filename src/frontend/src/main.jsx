/* external */
import ReactDOM from "react-dom/client";
import React from "react";
/* assets */
import "./assets/reset.css";
import "./assets/global.css";
/* internal */
import { UserProvider } from "./providers/UserProvider";
import Main from "./components/Main";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <UserProvider>
      <Main />
    </UserProvider>
  </React.StrictMode>
);
