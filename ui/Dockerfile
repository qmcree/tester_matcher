FROM node:8.4

# Install Yarn package manager.
RUN npm install --global yarn

# Create the source code directory.
ARG SOURCE_DIR=/usr/src/app/
RUN mkdir -p ${SOURCE_DIR}
WORKDIR ${SOURCE_DIR}

# Add the source code. If sharing code via volume, the code added at image build time is not used.
COPY . .

# Install Node modules via Yarn.
RUN yarn install

# Run the NPM script defined in the package.json to serve the application over port 3000.
CMD yarn run start
EXPOSE 3000