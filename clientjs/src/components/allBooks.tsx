import React, { useState, useEffect} from 'react';
import { useQuery } from '@apollo/client';
import { FETCH_ALL_BOOKS } from '../gql/query';

function AllBooks () {
    const [books, setBooks] = useState([{ id:0, title:"" }]);
    // useQuery will send query to backend through uri link and get the data
    const {  loading, error, data } = useQuery(FETCH_ALL_BOOKS);
    // body in useEffect will run after page is rendered and every time data state changed 
    // which is why console.log will run twice
    useEffect(() => {
        if(data){
            setBooks(data.allBooks.nodes);
            console.log(data.allBooks.nodes);
        }
    }, [data]);
    if (loading) console.log('Loading...');
    if (error) console.log(`Error! ${error.message}`);
    // map cycles through an array
    return (
        <div className="page2">
            <h1 className="title2">All Books</h1>
            <ol>
                {books.map((book) => (
                    <li>                
                        <a href={"http://localhost:3000/page?book=" + book.title}>{book.title}</a>
                    </li>
                ))}
            </ol>
        </div>
    )
}

export default AllBooks;



