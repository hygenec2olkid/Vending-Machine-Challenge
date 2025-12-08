import type { TestType } from "../../features/sample/type/api";
import Request from "../../shared/utils/request";

export const testGetData: () => Promise<TestType> = () => {
  return Request.get("");
};
