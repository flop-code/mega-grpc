import { BACKEND_URL, postQuery, getQuery, deleteQuery } from "./config"

export const api_create_post = async (data) => {
    const response = await postQuery(`${BACKEND_URL}/post/create`, data);
    return response;
};

export const api_get_all_posts = async () => {
    const response = await getQuery(`${BACKEND_URL}/post/all`);
    return response;
};

export const api_get_post_author = async (post_id) => {
    const response = await getQuery(`${BACKEND_URL}/post/${post_id}`);
    return response;
};

export const api_delete_post = async (post_id) => {
    const response = await deleteQuery(`${BACKEND_URL}/post/${post_id}`);
    return response;
}