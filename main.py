import time
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Live Updating Matplotlib Plot")

# Placeholder in the Streamlit page
plot_placeholder = st.empty()

# Example evolving data
x = np.linspace(0, 10, 100)

# Infinite update loop
for frame in range(1000):

    # Generate some changing data
    y = np.sin(x + frame * 0.2)

    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y)

    ax.set_ylim(-1.2, 1.2)
    ax.set_title(f"Frame {frame}")

    # Display in Streamlit
    plot_placeholder.pyplot(fig)

    # Important: close figure to avoid memory leak
    plt.close(fig)

    # Wait before next update
    time.sleep(1)
