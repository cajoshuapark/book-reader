import React, { useState, useEffect} from 'react';
import { useLocation } from "react-router-dom";
import { useQuery } from '@apollo/client';
import { FETCH_FIRST_PAGE } from '../gql/query';


function SearchResult () {
    const [allPages, setAllPages] = useState([{ pagenum:0,content:"" }]);
    const [currPage, setCurrPage] = useState({ pagenum:0,content:"" });
    const [bookId, setBookId] = useState(0);
    const [pageNum, setPageNum] = useState(0);
    // gets current location of the object
    const location = useLocation();
    //searches path for keyword book and queries the string after = sign    
    const query = new URLSearchParams(location.search).get("book");
    const [title, setTitle] = useState(query);

    // this hard coded part can be fixed by implementing either an intermediate page
    // or querying for page ID in search and send that information instead of title
    useEffect(() => {
        if(title === "Harry Potter"){
            setTitle("Harry Potter");
            setBookId(1);
        }else if(title === "Brisingr"){
            setTitle( "Brisingr");
            setBookId(2);
        }
    }, [title]);

    // useQuery will send query to backend through uri link and get the data
    const {  loading, error, data }  = useQuery(
        FETCH_FIRST_PAGE,{ variables: { id: bookId }}
    );
    // body in useEffect will run after page is rendered. 
    // it will also run when data is changed which is why it console.log twice
    useEffect(() => {
        if(data){
            setAllPages(data.bookById.pagesByBookId.nodes);
            setCurrPage(data.bookById.pagesByBookId.nodes[0]);
        }
    }, [data]);
    if (loading) console.log('Loading...');
    if (error) console.log(`Error! ${error.message}`);

    function getNextPage() {
        if(pageNum + 2 <= allPages.length){
            setCurrPage(allPages[pageNum+1]);
            setPageNum(pageNum + 1);
        }
    }

    function getPrevPage() {
        if(pageNum -1 >= 0){
            setCurrPage(allPages[pageNum-1]);
            setPageNum(pageNum - 1);
        }
    }
    return (
        <div className="page">
            <h1 className = "title">{title}</h1>
            <h2 className ="contents">{currPage.content}</h2>
            <h2 className ="pagenum-inpage">{currPage.pagenum}</h2>
            <button className = "circleBackButton" onClick={getPrevPage}>
              back page
            </button>
            <button className = "circleForwardButton" onClick={getNextPage}>
              next page
            </button>
        </div>
    )
}

export default SearchResult;





  // body in useEffect will run after page is rendered. 
  // useEffect(() => {
  //   // invalid url will trigger an 404 error
  //   const { search } = window.location;
  //   const query = new URLSearchParams(search).get('book');
  //   fetch("/getpage", {
  //     method:"POST",
  //     headers: {"Content-Type": "application/json" },
  //     body: JSON.stringify(query)
  //   }).then(res => res.json()
  //   ).then(
  //     currPage => {
  //       setData(currPage)
  //       // console.log(currPage)
  //     }
  //   )
  // }, []);

  // function getNextPage() {
  //   fetch("/nextpage", {
  //     method:"POST",
  //     headers: {"Content-Type": "application/json" },
  //     body: JSON.stringify(pageNum+1)
  //   }).then(res => res.json()
  //   ).then(
  //     currPage => {
  //       setData(currPage)
  //       // console.log(currPage)
  //     }
  //   );
  //   setPageNum(pageNum + 1);
  // };
  // function getPrevPage() {
  //   fetch("/nextpage", {
  //     method:"POST",
  //     headers: {"Content-Type": "application/json" },
  //     body: JSON.stringify(pageNum-1)
  //   }).then(res => res.json()
  //   ).then(
  //     currPage => {
  //       setData(currPage)
  //       // console.log(currPage)
  //     }
  //   );
  //   setPageNum(pageNum - 1);
  // }
