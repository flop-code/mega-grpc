/* external */
import { useContext, useState } from "react";
import { React } from "react";
import { useForm } from "react-hook-form";
/* assets */
/* internal */
import { api_current_user, api_login } from "../service/UserService";
import { UserContext } from "../providers/UserProvider";

const AuthForm = ({ setMainPage }) => {
  const { setUser } = useContext(UserContext);
  const [isSubmitting, setSubmitting] = useState(false);
  const [errorMsg, setErrorMsg] = useState(null);

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  const login = async (data) => {
    setSubmitting(true);
    let response = await api_login(data);
    setSubmitting(false);
    if (response.success) {
      response = await api_current_user();
      if (response.success) {
        setUser(response.data);
      } else { return setErrorMsg(response.message) }
    } else { return setErrorMsg(response.message) }
    setMainPage("home");
  };

  return (
    <form onSubmit={handleSubmit(login)} className="auth-form">
      <input type="text" {...register("username")} placeholder="Username" />
      <input type="password" {...register("password")} placeholder="Password" />
      <button type="submit" disabled={isSubmitting}>
        Submit
      </button>
      {errorMsg && <p style={{color: "#ff0000"}}>{errorMsg}</p>}
    </form>
  );
};

export default AuthForm;
