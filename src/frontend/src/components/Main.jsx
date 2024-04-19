/* external */
import { React, useContext, useEffect, useState } from "react";
/* assets */
/* internal */
import AuthForm from "./AuthForm";
import Articles from "./Articles";
import Header from "./Header";
import CreateArticle from "./CreateArticle";
import { UserContext } from "../providers/UserProvider";
import { api_current_user } from "../service/UserService";

const Main = () => {
  const { user, setUser } = useContext(UserContext);
  const [isMainPage, setMainPage] = useState("home");

  useEffect(() => {
    let wrapper = async () => {
      let response = await api_current_user();
      if (response.success) {
        setUser(response.data)
      }
    }
    wrapper();
  }, [])

  return (
    <>
      <Header setMainPage={setMainPage} />
      {isMainPage == "home" ? (
        <Articles />
      ) : isMainPage == "auth" ? (
        <AuthForm setMainPage={setMainPage} />
      ) : (
        <CreateArticle setMainPage={setMainPage} />
      )}
    </>
  );
};

export default Main;
