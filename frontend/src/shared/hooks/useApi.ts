import type { AxiosError } from "axios";
import { useCallback, useState } from "react";

type ApiResponse<T> = { pageable?: unknown } & T;

const useApi = <T = unknown, E = AxiosError>() => {
  const [data, setData] = useState<T | undefined>(undefined);
  const [errorMsg, setErrorMsg] = useState<E | undefined>(undefined);
  const [pageable, setPageable] = useState<unknown>(undefined);
  const [loading, setLoading] = useState(false);

  const makeRequest = useCallback(
    async (
      api: () => Promise<ApiResponse<T>>,
      params?: {
        dataTransformer?: (data: unknown) => T;
        isThrowError?: boolean;
      }
    ) => {
      setLoading(true);
      try {
        const apiResponse = await api();

        const transformed = params?.dataTransformer
          ? params.dataTransformer(apiResponse)
          : apiResponse;
        setData(transformed);

        const responsePageable = apiResponse.pageable;
        setPageable(responsePageable ?? undefined);

        return apiResponse;
      } catch (error: unknown) {
        console.error(error);
        if (error instanceof Error && 'isAxiosError' in error && (error as AxiosError).isAxiosError) {
          setErrorMsg((error as E));
        }

        if (params?.isThrowError) throw error;

        return error;
      } finally {
        setLoading(false);
      }
    },
    []
  );

  return {
    makeRequest,
    data,
    errorMsg,
    pageable,
    loading,
    onSetData: setData,
    onSetPageable: setPageable,
    onSetLoading: setLoading,
    onSetErrorMsg: setErrorMsg,
  };
};

export default useApi;
