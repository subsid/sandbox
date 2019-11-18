const jexiaSDK = require("jexia-sdk-js/node"); 
const dataModule = jexiaSDK.dataOperations();

const credentials = {
  projectID: "ca020507-60c9-440d-9f43-1f615d290117",
  key: "de4a02a0-6339-4df9-9f02-94a38f27090f",
  secret: "laFrl2w0wtjB4ggVYKGsLr2lHv1bkNUnryP0AdTfHWKzdT6xKwq4JVk2TozafYc5hOwdCMIebi4pxDEVwMKmWg==",
};

jexiaSDK.jexiaClient().init(credentials, dataModule);

const items = dataModule.dataset("items")

// items.insert([
//   {title: "Todo1", status: "TODO"},
//   {title: "Todo2", status: "DONE"},
//   {title: "Todo3", status: "NULL"}
// ])
// .execute()
// .then((records) => {
//   console.log("Done", records)
// }).catch((e) => {
//   console.log("oops");
//   console.log(e);
// })


