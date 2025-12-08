import { useEffect } from "react";

import { useNavigate } from "react-router";
import { testGetData } from "../../apis/sample";
import useApi from "../../shared/hooks/useApi";
import type { TestType } from "./type/api";

function Home() {
  const { makeRequest, data, loading } = useApi<TestType>();

  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = () => {
      makeRequest(() => testGetData());
    };

    fetchData();
  }, [makeRequest]);

  return (
    <>
      This is Home page
      <br />
      {loading ? "loading..." : data?.fact}
      <br />
      <button onClick={() => navigate("/contact")} className="bg-red-200 p-2">
        go to contact page
      </button>
    </>
  );
}

export default Home;
