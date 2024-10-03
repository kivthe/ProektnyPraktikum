const ItemList = () => {
    const my_list = ["asd", "fgh", "jkl"]

    const items = my_list.map(item => <p>{item}</p>)

    return (
        <>
            <h1>More items</h1>

            <div>
                <p>List:</p>

                <div>
                    {items}
                </div>
            </div>
        </>
    )
}

export default ItemList;