import { createContext, useEffect, useState } from "react";
// import { api_current_user } from "../services/ApiAuth";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // useEffect(() => {
  //   api_current_user().then((response) => {
  //     setUser(response.success ? response.data : null);
  //   });
  // }, []);

  return <UserContext.Provider value={{ user, setUser }}>{children}</UserContext.Provider>;
};
