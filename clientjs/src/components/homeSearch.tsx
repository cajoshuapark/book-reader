import React from "react";

// Home page big input
function HomeSearch () {
    return (
        <form action="/page" method="get">
        <input
            type="text"
            placeholder="Search books"
            className = "introInput"
            name = "book"
        />
        <button 
            className = "introSearch"
            >Search
        </button>
    </form>
    )
};
export default HomeSearch;
