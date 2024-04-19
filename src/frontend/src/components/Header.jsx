/* external */
import { useState } from "react";
import { React, useContext } from "react";
/* assets */
/* internal */
import { UserContext } from "../providers/UserProvider";
import { api_logout } from "../service/UserService";

const Header = ({ setMainPage }) => {
  const { user, setUser } = useContext(UserContext);
  const [ isSubmitting, setSubmitting ] = useState(false);


  const logout = async () => {
    setSubmitting(true);
    let response = await api_logout();
    if (response.success) {
      setUser(null);
    }
    setSubmitting(false);
  };

  return (
    <header>
      <div onClick={() => setMainPage("home")} className="logo">
        PostHub
      </div>
      {user && <button onClick={() => setMainPage("article")}>Create article</button>}
      <div className="actions">
        {user ? (
          <button onClick={logout} disabled={isSubmitting}>
            Logout
          </button>
        ) : (
          <button onClick={() => setMainPage("auth")}>Sign In</button>
        )}
      </div>
    </header>
  );
};

export default Header;
