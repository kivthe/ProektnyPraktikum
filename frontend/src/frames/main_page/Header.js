import "./Header.css"

const Header = ({ contacts, children }) => {

    

    return (
        <div className="main_container">
            <h1> {children} </h1>

            <div>
                <a>
                    <img />
                </a>

                <a>
                    <img />
                </a>

                <a>
                    <img />
                </a>
            </div>
        </div>
    )
}

export default Header;