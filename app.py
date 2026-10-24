
import streamlit as st
import string

st.set_page_config(
    page_title="Password Security",
    page_icon="🔐",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #151b2e);
    color: #f1f5f9;
}
.block-container {
    max-width: 750px;
    padding-top: 3rem;
}
h1, h2, h3, p, label {
    color: #f1f5f9 !important;
}
.security-card {
    background: #1b2438;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #34415c;
    margin: 12px 0;
}
.subtitle {
    color: #aab6cc !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center'>🔐 Password Security</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p class='subtitle'>Your password. Your security. Check it instantly.</p>",
    unsafe_allow_html=True
)

st.markdown('<div class="security-card">', unsafe_allow_html=True)
password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Type a password here..."
)
st.markdown('</div>', unsafe_allow_html=True)

if password:
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letter (A-Z)": any(c.isupper() for c in password),
        "Lowercase letter (a-z)": any(c.islower() for c in password),
        "At least one number (0-9)": any(c.isdigit() for c in password),
        "Special character (!@#$...)": any(
            c in string.punctuation for c in password
        ),
    }

    score = sum(checks.values())

    st.markdown('<div class="security-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Security Checklist")

    for label, passed in checks.items():
        if passed:
            st.markdown(f"🟢 {label}")
        else:
            st.markdown(f"🔴 {label}")

    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Password Strength")
    st.progress(score / len(checks))

    if score <= 2:
        st.error("Weak — try adding more security features.")
    elif score <= 4:
        st.warning("Medium — improve the remaining checks.")
    else:
        st.success("Strong — all five checks passed!")

    st.caption(
        "Demo checker: this score uses simple rules and "
        "does not guarantee that a password is secure."
    )
else:
    st.info("Enter a password above to begin the security check.")

st.markdown("---")
st.caption("🔒 Password Security Checker | Python + Streamlit")
