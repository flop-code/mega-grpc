/* external */
import { useContext, useState } from "react";
import { React } from "react";
import { useForm } from "react-hook-form";
/* assets */
/* internal */
import { UserContext } from "../providers/UserProvider";
import { api_create_post } from "../service/PostService";

const CreateArticle = ({ setMainPage }) => {
  const { setUser } = useContext(UserContext);
  const [isSubmitting, setSubmitting] = useState(false);
  const [errorMsg, setErrorMsg] = useState(null);

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  const createArticle = async (data) => {
    setSubmitting(true);
    let response = await api_create_post(data);
    setSubmitting(false);
    if (!response.success) {
      return setErrorMsg(response.message);
    }
    setMainPage("home");
  };

  return (
    <form onSubmit={handleSubmit(createArticle)} className="auth-form">
      <input type="text" {...register("title")} placeholder="Title" />
      <button type="submit" disabled={isSubmitting}>
        Submit
      </button>
      {errorMsg && <p style={{color: "#ff0000"}}>{errorMsg}</p>}
    </form>
  );
};

export default CreateArticle;
