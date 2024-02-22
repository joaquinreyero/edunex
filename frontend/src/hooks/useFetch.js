import { useState, useEffect } from "react"

const useFetch = (url) => {
    const [state, setState] = useState({
        data: null,
        isLoading: true,
        errors: null
    })

    const getFetch = async () => {
        try {
            const response = await fetch(url)
            const data = await response.json()
            setState({
                data: data,
                isLoading: false,
                errors: null
            })
        } catch (errors) {
            setState({
                data: null,
                isLoading: false,
                errors: errors
            })
        }
    }

    useEffect(() => {
        if (!url) return
        getFetch()
    }, [url])

    return [state.data, state.isLoading, state.errors];
}

export default useFetch;
