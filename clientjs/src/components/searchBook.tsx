import React from 'react';

function Search () {
    // redirect to a different path which is urlSearchParam compatible
    // this is done so that infinite rendering does not occur with the useEffect hook
  return (
        <form action="/page" method="get">
        <input
            type="text"
            name="book"
            placeholder="Search books"
            className="topInput"
        />
        <button 
            className = "search"
        >Search
        </button>
    </form>
    )
};
export default Search;
