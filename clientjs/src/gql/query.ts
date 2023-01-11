import { gql } from "@apollo/client";

export const FETCH_ALL_BOOKS = gql `
  query getBookId {
    allBooks{
      nodes{
        id
        title
      }
    }
  }
`;



export const FETCH_FIRST_PAGE = gql `
  query test3($id: Int!) {
    bookById(id: $id){
      pagesByBookId{
        nodes{
          pagenum
          content
        }
      }
    }
  }
`;
