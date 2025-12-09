import { useEffect, useState } from "react";
import { buyItem, getProductList } from "../../apis/product";
import useApi from "../../shared/hooks/useApi";
import type {
  AddCoinIntoStockRequest,
  BuyProductRequest,
  Coin,
  Product,
} from "./type/api";
import { addCoin } from "../../apis/coin";

function MainPage() {
  const { makeRequest, data, loading } = useApi<Product[]>();
  const {
    makeRequest: buyItemApi,
    data: returnCoin,
    loading: isPendingPayment,
    errorMsg,
    onSetData,
  } = useApi<Record<number, number>>();
  const { makeRequest: addCoinApi } = useApi<Coin[]>();

  const [item, setItem] = useState<Product | null>(null);
  const [balance, setBalance] = useState<number>(0);

  const coinType = [1, 5, 10, 50, 100, 500, 1000];

  useEffect(() => {
    const fetchData = () => {
      makeRequest(() => getProductList());
    };

    fetchData();
  }, [makeRequest]);

  const onSelectItem = (item: Product) => {
    if (item.quantity <= 0) return;
    setItem(item);
  };

  const onBuyItem = () => {
    const payload: BuyProductRequest = {
      id: item?.id ?? 0,
      quality: 1,
      balance: balance,
    };
    buyItemApi(() => buyItem(payload));
  };

  useEffect(() => {
    setBalance(0);
    setItem(null);
  }, [returnCoin]);

  useEffect(() => {
    if (errorMsg) {
      onSetData(undefined);
      setBalance(0);
      setItem(null);
      alert(
        errorMsg.response?.data &&
          typeof errorMsg.response.data === "object" &&
          "detail" in errorMsg.response.data
          ? (errorMsg.response.data as { detail: string }).detail
          : "An error occurred during the transaction."
      );
    }
  }, [errorMsg, onSetData]);

  const isDisabled = () =>
    balance === 0 || (item?.price ?? 0) <= 0 || balance < (item?.price ?? 0);

  const onAddCoin = () => {
    const payloads: AddCoinIntoStockRequest[] = coinType.map((coin) => {
      return {
        coin: coin,
        quantity: 10,
      };
    });

    payloads.forEach((p) => addCoinApi(() => addCoin(p)));
    alert("Added coins into stock");
  };

  return (
    <>
      <header className="text-center py-5 text-2xl">Wirapat Shop</header>

      <div className="flex bg-gray-custom">
        <div className="w-[25%] p-2">
          <button
            className="bg-blue-500 px-3 py-1 text-white rounded-xl mt-1 mb-4 cursor-pointer"
            onClick={() => onAddCoin()}
          >
            Add coin
          </button>
          <p>Add money:</p>
          {coinType.map((coin) => (
            <button
              key={coin}
              className="bg-green-500 text-white m-2 p-2"
              onClick={() => setBalance((prev) => prev + coin)}
            >
              {coin} ฿
            </button>
          ))}
          <div className="mt-12 flex flex-col gap-2">
            <p>Balance: {balance} ฿</p>
            <p>Item: {item ? item.price : 0} ฿</p>
            {isPendingPayment ? (
              "process..."
            ) : (
              <button
                className={`text-white p-2 w-full 
                ${isDisabled() ? "bg-gray-400" : "bg-blue-500 cursor-pointer"}
                `}
                disabled={isDisabled()}
                onClick={() => onBuyItem()}
              >
                Payment
              </button>
            )}
          </div>

          {returnCoin && (
            <div className="text-center mt-5 text-green-500">
              Got money return:{" "}
              {Object.entries(returnCoin).reduce((total, [coin, count]) => {
                // 💡 Key Change: Convert coin string to a number and multiply by count
                return total + Number(coin) * count;
              }, 0)}{" "}
              ฿
            </div>
          )}
        </div>
        <div className="w-[75%] grid grid-cols-3 gap-3 p-2">
          {loading
            ? "loading..."
            : data?.map((product) => (
                <div
                  key={product.id}
                  className={`p-4 border text-center border-gray-300  
                    ${
                      product.quantity > 0
                        ? "hover:shadow-lg cursor-pointer bg-white"
                        : "opacity-50"
                    }
                    `}
                  onClick={() => onSelectItem(product)}
                >
                  <img
                    src={product.img_url}
                    alt={product.name}
                    className="w-40 h-40 object-cover mb-2 block mx-auto"
                  />
                  <p> {product.name}</p>
                  <p> ฿ {product.price}</p>
                </div>
              ))}
        </div>
      </div>
    </>
  );
}

export default MainPage;
