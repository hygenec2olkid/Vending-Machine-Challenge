import { useNavigate } from "react-router";

function Contact() {
  const navigate = useNavigate();
  return (
    <>
      This is Contact page
      <br />
      <button onClick={() => navigate("/")} className="bg-red-200 p-2">
        go to contact page
      </button>
    </>
  );
}

export default Contact;
