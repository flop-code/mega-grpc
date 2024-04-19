/* external */
import { React, useContext, useEffect, useState } from "react";
import { api_get_all_posts, api_get_post_author, api_delete_post } from "../service/PostService";
/* assets */
/* internal */

const Article = ({ data }) => {
  const { id, title } = data;
  const [isDetail, setDetail] = useState(false);
  const [author, setAuthor] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);

  const loadMoreInfo = async () => {
    if (author) return;
    let response = await api_get_post_author(id);
    if (!response.success) { return setErrorMsg(response.message) }
    setAuthor(response.data);
  };

  const switchDetail = async () => {
    if (!isDetail) await loadMoreInfo();
    setDetail(!isDetail);
  };

  const doDelete = async () => {
    let response = await api_delete_post(id);
    if (!response.success) { return setErrorMsg(response.message) }
  };

  return (
    <article>
      <div>
        <h1>
          {id}. {title}
        </h1>
        <p>{isDetail && `Author: ${author.username}, ${author.phone_number}, ${author.address}`}</p>
        {errorMsg && <p style={{color: "#ff0000"}}>{errorMsg}</p>}
      </div>
      <button onClick={switchDetail}>{isDetail ? "Less details" : "More details"}</button>
      <button onClick={doDelete}>Delete</button>
    </article>
  );
};

const Articles = () => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    let wrapper = async () => {
      let response = await api_get_all_posts();
      if (response.success) setArticles(response.data.posts);
    }
    wrapper()
  }, [])

  return (
    <div className="articles">
      {articles.map((article, index) => (
        <div className={index % 2 == 0 ? "article-1" : "article-2"} key={index}>
          <Article key={index} data={article} />
        </div>
      ))}
    </div>
  );
};

export default Articles;
