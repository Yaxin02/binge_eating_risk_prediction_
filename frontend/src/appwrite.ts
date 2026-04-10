import { Client, Databases, Functions, ID } from "appwrite";

const client = new Client();

client
    .setEndpoint(
      import.meta.env.VITE_APPWRITE_ENDPOINT || "https://nyc.cloud.appwrite.io/v1"
    )
    .setProject(import.meta.env.VITE_APPWRITE_PROJECT_ID || "69d8f483003b02a74713");

export const databases = new Databases(client);
export const functions = new Functions(client);
export { ID };

export const APPWRITE_DATABASE_ID =
  import.meta.env.VITE_APPWRITE_DATABASE_ID || "binge_db";
export const APPWRITE_COLLECTION_ID =
  import.meta.env.VITE_APPWRITE_COLLECTION_ID || "patients";
/** Set VITE_APPWRITE_FUNCTION_ID on the host, or run `appwrite pull functions` and commit appwrite.config.json. */
export const APPWRITE_FUNCTION_ID =
  import.meta.env.VITE_APPWRITE_FUNCTION_ID || "predict";
