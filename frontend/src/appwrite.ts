import { Client, Databases, Functions, ID } from "appwrite";

const client = new Client();

client
    .setEndpoint(import.meta.env.VITE_APPWRITE_ENDPOINT || 'https://cloud.appwrite.io/v1')
    .setProject(import.meta.env.VITE_APPWRITE_PROJECT_ID || 'PENDING_PROJECT_ID');

export const databases = new Databases(client);
export const functions = new Functions(client);
export { ID };

export const APPWRITE_DATABASE_ID = import.meta.env.VITE_APPWRITE_DATABASE_ID || 'PENDING_DB_ID';
export const APPWRITE_COLLECTION_ID = import.meta.env.VITE_APPWRITE_COLLECTION_ID || 'PENDING_COLLECTION_ID';
export const APPWRITE_FUNCTION_ID = import.meta.env.VITE_APPWRITE_FUNCTION_ID || 'PENDING_FUNCTION_ID';
